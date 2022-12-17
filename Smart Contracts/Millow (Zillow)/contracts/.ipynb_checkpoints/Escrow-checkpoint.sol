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


// Sets all the variables in the constructor 

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
