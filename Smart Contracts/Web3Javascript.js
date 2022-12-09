// We can monitor the smart contract using Web3.js.  This script is to connect to the smart contract using Web3.js

const Web3 = require('Web3');

const web3 = new Web3('https://mainnet.infura.io/v3/9160550b11aa4acdbd1ca763edb48a52') // Infura HTTP

web3.eth.accounts.wallet.add('') // Add Private Key to send transactions

web3.eth.getBalance('').then(balance => console.log(balance)); //

const contract = new web3.eth.Contract(abi, '') // Add in account. ABI: Description of the contract 


contract.methods.read().call().then(result => console.log(result)); // read() is the function that is in the other file.  See example below

web3.eth.sendTransaction({from: '', value: 1000}) // add in account from getBalance

contract.methods.write().sendTransaction({from: ''}); // Add in account from sendTransaction


// Youtube Video with Instructions https://www.youtube.com/watch?v=b41OPU0-4bY

// myContract Example for contract.methods.read()


pragma solidity 0.8.0;

contract Mycontractol {
    uint data;

    funciton read() external view returns(uint){
        return data;

    }
} //