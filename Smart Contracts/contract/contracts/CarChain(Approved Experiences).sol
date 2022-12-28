// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract CarChain {

    address owner; // Whoever deploys smart contract is the owner
    uint ownerBalance;

    constructor() {
        owner = msg.sender;
    }

    // Constructor goes before Sudo Code.

    // Add yourself as a Renter

    // Add yourself as a Renter
    struct Renter {
        address payable walletAddress; // Payable ensures that the function can send and receive Ether
                                      // Address corresponds to the last 20 bytes of the Keccak-256 hash of the public key
        string firstName;
        string lastName;
        bool canRent;
        bool active;
        uint balance; // Send money to balance to cover fees
        uint due;
        uint start; // Start of renting
        uint end; // End of renting
    }

    mapping (address => Renter) public renters;

    function addRenter(address payable walletAddress, string memory firstName, string memory lastName, bool canRent, bool active, uint balance, uint due, uint start, uint end) public {
        renters[walletAddress] = Renter(walletAddress, firstName, lastName, canRent, active, balance, due, start, end);
    }

        // Key above is Renters Wallet Address and the Value is Renter(walletAddress, firstName, lastName, canRent, active, balance, due, start, end).
        // Funciton above pushes a renter to the dictionary (mapping).

    modifier isRenter(address walletAddress) {
        require(msg.sender == walletAddress, "You can only manage your account");
        _;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "You are not allowed to access this");
        _;
    }

    // Memory in Solidity is a temporary place to store data whereas Storage holds data between function calls.

    // Rent Car
    function checkOut(address walletAddress) public isRenter(walletAddress) {
        require(renters[walletAddress].due == 0, "You have a pending balance."); // Can't checkout unless balance is paid.
        require(renters[walletAddress].canRent == true, "You cannot rent at this time.");
        renters[walletAddress].active = true;
        renters[walletAddress].start = block.timestamp; // Unix Timestamp in Uint is marked in start variable
        // renters[walletAddress].canRent = false; // Once you rent a car you can no longer rent unless we want them to be able to rent more than one vehicle
        renters[walletAddress].canRent = false;
    }

    // Check in a Car
    function checkIn(address walletAddress) public isRenter(walletAddress) {
        require(renters[walletAddress].active == true, "Please check out a Car first.");  // Car is rented so it is active.  If not active no car to return.
        renters[walletAddress].active = false; // Renter is no longer active
        renters[walletAddress].end = block.timestamp; // Unix Timestamp is marked in End Variable
        setDue(walletAddress);
    }

    // Get total duration of Car use (This function will be used within other functions)
    function renterTimespan(uint start, uint end) internal pure returns(uint) { // Internal to contract and doesnt alter the contract outside of this function.  Pure means that we are not touching any variables because we are passing in these two variables
        return end - start;
    }

    function getTotalDuration(address walletAddress) public isRenter(walletAddress) view returns(uint) {
        if (renters[walletAddress].start == 0 || renters[walletAddress].end == 0) {
            return 0;
        } else {
            uint timespan = renterTimespan(renters[walletAddress].start, renters[walletAddress].end);
            uint timespanInMinutes = timespan / 60;
            return timespanInMinutes;
        }
    }

    // Get Contract balance
    function balanceOf() view public onlyOwner() returns(uint) {
        return address(this).balance;
    }

    function getOwnerBalance() view public onlyOwner() returns(uint) {
        return ownerBalance;
    }

    function withdrawOwnerBalance() payable public {
        payable(owner).transfer(ownerBalance);
    }

    // Get Renter's balance
    function balanceOfRenter(address walletAddress) public isRenter(walletAddress) view returns(uint) {
        return renters[walletAddress].balance;
    }

    // Set Due amount
    function setDue(address walletAddress) internal {
        uint timespanMinutes = getTotalDuration(walletAddress);
        uint fiveMinuteIncrements = timespanMinutes / 5;
        renters[walletAddress].due = fiveMinuteIncrements * 5000000000000000;
    }


    // True or False if renter can rent car or not.  (Variable above for canRent)
    function canRentCar(address walletAddress) public isRenter(walletAddress) view returns(bool) {
        return renters[walletAddress].canRent;
    }

    // Deposit
    function deposit(address walletAddress) isRenter(walletAddress) payable public {
        renters[walletAddress].balance += msg.value; // Value will be picked up in the global msg.value
    }

    // Make Payment
    function makePayment(address walletAddress, uint amount) public isRenter(walletAddress) {
        require(renters[walletAddress].due > 0, "You do not have anything due at this time."); // Don't want people paying anything if they don't owe.
        require(renters[walletAddress].balance > amount, "You do not have enough funds to cover payment. Please make a deposit."); // Have to deposit money and then transfer as funds
        renters[walletAddress].balance -= amount;
        ownerBalance += amount;
        renters[walletAddress].canRent = true;
        renters[walletAddress].due = 0;
        renters[walletAddress].start = 0;
        renters[walletAddress].end = 0;
    }

    function getDue(address walletAddress) public isRenter(walletAddress) view returns(uint) {
        return renters[walletAddress].due;
    }

    function getRenter(address walletAddress) public isRenter(walletAddress) view returns(string memory firstName, string memory lastName, bool canRent, bool active) {
        firstName = renters[walletAddress].firstName;
        lastName = renters[walletAddress].lastName;
        canRent = renters[walletAddress].canRent;
        active = renters[walletAddress].active;
    }

    function renterExists(address walletAddress) public isRenter(walletAddress) view returns(bool) {
        if (renters[walletAddress].walletAddress != address(0)) {
            return true;
        }
        return false;
    }

}