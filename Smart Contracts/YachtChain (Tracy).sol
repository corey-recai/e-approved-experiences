

pragma solidity ^0.8.0;

contract YachtChain {

    address owner; // Whoever deploys smart contract is the owner

    constructor() {
        owner = msg.sender; // This constructor runs when its first deployed.  The sender who is deploying it is set as the owner.
    }
    // Constructor goes before Sudo Code.

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

    mapping (address => Renter) public renters; // Key-Value Pair Key: Address and Value: Renter.  When Address is given renter is called.

    function addRenter(address payable walletAddress, string memory firstName, string memory lastName, bool canRent, bool active, uint balance, uint due, uint start, uint end) public {
        renters[walletAddress] = Renter(walletAddress, firstName, lastName, canRent, active, balance, due, start, end);
    }

        // Key above is Renters Wallet Address and the Value is Renter(walletAddress, firstName, lastName, canRent, active, balance, due, start, end).
        // Funciton above pushes a renter to the dictionary (mapping).



    // Memory in Solidity is a temporary place to store data whereas Storage holds data between function calls.

    // Rent Yacht
    function RentOut(address walletAddress) public {
        require(renters[walletAddress].due == 0, "You have a pending balance."); // Can't checkout unless balance is paid.
        require(renters[walletAddress].canRent == true, "You cannot rent at this time.");
        renters[walletAddress].active = true;
        renters[walletAddress].start = block.timestamp; // Unix Timestamp in Uint is marked in start variable
        // renters[walletAddress].canRent = false; // Once you rent a car you can no longer rent unless we want them to be able to rent more than one vehicle
    }

    // Return a yacht
    function Return(address walletAddress) public {
        require(renters[walletAddress].active == true, "Please rent a Car first."); // Car is rented so it is active.  If not active no car to return.
        renters[walletAddress].active = false; // Renter is no longer active
        renters[walletAddress].end = block.timestamp; // Unix Timestamp is marked in End Variable
        setDue(walletAddress);
    }

    // Get total duration of Yacht use (This function will be used within other functions)
    function renterTimespan(uint start, uint end) internal pure returns(uint) { // Internal to contract and doesnt alter the contract outside of this function.  Pure means that we are not touching any variables because we are passing in these two variables
        return end - start;
    }

    function getTotalDurationDays(address walletAddress) public view returns(uint) {
        require(renters[walletAddress].active == false, "Car is currently rented out.");
        uint timespan = renterTimespan(renters[walletAddress].start, renters[walletAddress].end); // Referenced Function above for Duration (renterTimespan)
        uint timespanInMinutes = timespan / 60; // Turns Timespan into Minutes.
        uint timespaninHours = timespan / 3600; // Turns Timespan into Hours.
        uint timespaninDays = timespan / 86400; // Turns Timespan into Days.
        uint timespaninMonths = timespan / 2629743; // Turns Timespan into Months.
        uint timespaninYears= timespan / 31556926; // Turns Timespan into Years.
        return timespaninDays; // 
    }
    
    function getTotalDurationHours(address walletAddress) public view returns(uint) {
        require(renters[walletAddress].active == false, "Car is currently rented out.");
        uint timespan = renterTimespan(renters[walletAddress].start, renters[walletAddress].end); // Referenced Function above for Duration (renterTimespan)
        uint timespanInMinutes = timespan / 60; // Turns Timespan into Minutes.
        uint timespaninHours = timespan / 3600; // Turns Timespan into Hours.
        uint timespaninDays = timespan / 86400; // Turns Timespan into Days.
        uint timespaninMonths = timespan / 2629743; // Turns Timespan into Months.
        uint timespaninYears= timespan / 31556926; // Turns Timespan into Years.
        return timespaninHours; // 
    }

    // Get Contract balance
    function balanceOf() view public returns(uint) {
        return address(this).balance;
    }

    // Get Renter's balance
    function balanceOfRenter(address walletAddress) public view returns(uint) {
        return renters[walletAddress].balance;
    }

    // Set Due amount hourly (Yachts are by 4 / 6 / 8 Hourse and Days).  Will need functions and if statements based on Hours or Day for Yachts.
    function setDueHourly(address walletAddress, uint amountPerHour) internal { // Internal won't let anyone else change or modify the function.
        uint hourlytimespan = getTotalDurationHours(walletAddress);
        renters[walletAddress].due = hourlytimespan * amountPerHour; // Multiply Hourly Timespan * amount per hour.  Check if hourly rate is different by amount of hours and days.
    }

    // Set Due amount Daily (Yachts are by 4 / 6 / 8 Hourse and Days).  Will need functions and if statements based on Hours or Day for Yachts.
    function setDue(address walletAddress, uint amountPerDay) internal { // Internal won't let anyone else change or modify the function.
        uint timespanDays= getTotalDurationDays(walletAddress);
        renters[walletAddress].due = timespanDays * amountPerDay; // Multiply Hourly Timespan * amount per hour.  Check if hourly rate is different by amount of hours and days.
    }

    // Hourly and Daily rates will be in Python Dictionary


    // True or False if renter can rent car or not.  (Variable above for canRent)
    function canRentYacht(address walletAddress) public view returns(bool) {
        return renters[walletAddress].canRent;
    }

    // Deposit
    function deposit(address walletAddress) payable public {
        renters[walletAddress].balance += msg.value; // Value will be picked up in the global msg.value
    }

    // Make Payment
    function makePayment(address walletAddress) payable public {
        require(renters[walletAddress].due > 0, "You do not have anything due at this time."); // Don't want people paying anything if they don't owe.
        require(renters[walletAddress].balance > msg.value, "You do not have enough funds to cover payment. Please make a deposit."); // Have to deposit money and then transfer as funds
        renters[walletAddress].balance -= msg.value;
        renters[walletAddress].canRent = true;
        renters[walletAddress].due = 0;
        renters[walletAddress].start = 0;
        renters[walletAddress].end = 0;
    }



    

}