//SPDX-License-Identifier: Unlicense
// Seller can list a property and a buyer can show their intent to buy and leave a downpayment
// Lender, Inspector, and Appraiser can get involved.


pragma solidity ^0.8.0;

interface IERC721 {
    function transferFrom(
        address _from,
        address _to,
        uint256 _id
    ) external;
}

contract Escrow {
    address public nftAddress;
    address payable public seller; // address is payable because Ether will be transferred to them 
    address public inspector;
    address public lender; // data type is address lender is the variable name and public means variable is visible outside the smart contract

    modifier onlySeller() {
        require(msg.sender) == seller, "Only seller can call this method");
        _;
    }

    // First uint256 on left is the id of the NFT

    mapping(uint256 => bool) public isListed;
    mapping(uint256 => uint256) public purchasePrice;
    mapping(uint256 => uint256) public escrowAmount;
    mapping(uint256 => address) public buyer;  // Should non crypto users have Address
    mapping(uint256 => bool) public inspectionPassed;

// Sets all the variables in the constructor.  A constructor initializes state variables of a contract

    constructor(
        
        address _nftAddress, 
        address payable _seller, 
        address _inspector, 
        address _lender
    ) {
        // Pass in variables
        nftAddress = _nftAddress;
        seller = _seller;
        inspector = _inspector;
        lender = _lender;
    }
}   

// A function is a group of reusable code which can be called anywhere in your program.

    function list(
        
        uint256 _nftID, 
        address _buyer, 
        uint256 _purchasePrice,
        uint256 _escrowAmount
    ) public payable onlySeller {
    
        // Transfer NFT from seller to this contract (Approved Experiences Owns the NFT initially then sent to Escrow account)
        IERC721(nftAddress).transferFrom(msg.sender, address(this), _nftID);

        isListed[_nftID] = true;
        purchasePrise[_nftID] = _purchasePrice;
        escrowAmount[_nftID] = _escrowAmount;
        buyer[_nftID] = _buyer;
    }

     // Put Under Contract (only buyer - payable escrow)
        function depositEarnest(uint256 _nftID) public payable onlyBuyer(_nftID) {
            require(msg.value >= escrowAmount[_nftID]);
    }

    // Update Inspection Status (only inspector): (Will become Car Inspection Status)
    function updateInspectionStatus(uint256 _nftID, bool _passed)
        public
        onlyInspector
    {
        inspectionPassed[_nftID] = _passed;
    }

    // Approve Sale (Will become Approve to Return)
    function approveSale(uint256 _nftID) public {
        approval[_nftID][msg.sender] = true;

    receive() external payable {}

    function getBalance() public view returns (uint256) {
        return address(this).balance
    }

    // Finalize Sale
    // -> Require inspection status (add more items here, like appraisal)
    // -> Require sale to be authorized
    // -> Require funds to be correct amount
    // -> Transfer NFT to buyer
    // -> Transfer Funds to Seller

    function finalizeSale(uint256 _NFTID) public {
        require(inspectionPassed[_NFTID]);
        require(approval[_nftID][buyer[_nftID]]);
        require(approval[_nftID][seller]);
        require(approval[_nftID][lender]);
        require(address(this).balance >= purchasePrice[_nftID];

        // The money is sent to Seller (Will be money sent to Approved Experiences and Deposit returned to Renter)
        // Add a smart contract to send deposit back to Renter or include deposit return in the function

        (bool success, ) = payable(seller).call{value: address(this).balance}("");
        require(success);


        // This is not needed because the buyer doesnt need a NFT but rather a sales Reciept.

        IERC721(nftAddress).transferFrom(address(this), buyer[_nftID], _nftID);

    }

    // Cancel Sale (handle earnest deposit)
    // -> if inspection status is not approved, then refund, otherwise send to seller
    function cancelSsale(uint256 _nftID) public {
        if (inspectionPassed[_nftID] == false) {
            payable(buyer[_nftID]).transfer(address(this).balance);

        } else {
            payable(seller).transfer(address(this).balance);
        }
    }

    receive() external payable {}

    function getBalance() public view returns (uint256) {
        return address(this).balance
    }

}