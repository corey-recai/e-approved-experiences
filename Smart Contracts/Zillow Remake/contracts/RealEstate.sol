//SPDX-License-Identifier: Unlicense
// Creating NFT using 3rd Party Library (https://docs.openzeppelin.com/contracts/2.x/erc721)

pragma solidity ^0.8.0;

import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";

contract RealEstate is ERC721URIStorage {
    using Counters for Counters.Counter; // Inumerable contract that Mints NFT from scratch by 
    Counters.Counter private _tokenIds;

    constructor() ERC721Full("Real Estate", "REAL") {
    
    function mint(string memory tokenURI) public returns (uint256) {
        _tokenIds.increment();

        uint256 newItemId = _tokenIds.current();
        _mint(msg.sender, newItemId);
        _setTokenURI(newItemId, tokenURI);

        return newItemId

    }

    function totalSupply() public view returns (uint256) {
        return _tokenIds.current();
    }
    }

}
