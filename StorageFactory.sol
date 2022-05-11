// SPDX-License-Identifier: MIT

//always give the version
pragma solidity ^0.6.0;

import "./SimpleStorage.sol"; 

// iheritence by `is` keyword
contract StorageFactory is SimpleStorage{

    SimpleStorage[] public simpleStorageArray;

    function createSimpleStorageContract() public{
        SimpleStorage simpleStorage = new SimpleStorage();
        simpleStorageArray.push(simpleStorage);
    }

    function sfStore(uint256 _simpleStorageIndex, uint256 _simpleStorageNumber) public{
        //Address & ABI->application binary interface

        // SimpleStorage simpleStorage = SimpleStorage(address(simpleStorageArray[_simpleStorageIndex]));
        // simpleStorage.store(_simpleStorageNumber);
        //we can do above and below as well
        SimpleStorage(address(simpleStorageArray[_simpleStorageIndex])).store(_simpleStorageNumber);

    }

    function sfGet(uint256 _simpleStorageIndex) public view returns(uint256){
        // SimpleStorage simpleStorage = SimpleStorage(address(simpleStorageArray[_simpleStorageIndex]));
        // return simpleStorage.retrieve();
        //we can do above and below as well
        return SimpleStorage(address(simpleStorageArray[_simpleStorageIndex])).retrieve();
    }
}