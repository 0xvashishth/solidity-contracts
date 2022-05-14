// SPDX-License-Identifier: MIT

//always give the version
pragma solidity ^0.6.0;


contract SimpleStorage{

    uint256 favouriteNumber;
    bool favouriteBool;
    // bool  favouriteBool2;
    // bool favouriteBool = false;
    // string favouriteString = "String";
    // int256 favouriteInt = -5;
    // address favouriteAddress = 0xa62d5D83B71419626FE359C2a6b39cC975C9706d
    // bytes32 favouritebytes = "cat"

    struct People{
        uint256 favouriteNumber;
        string name;
    }

    // People public person = People({favouriteNumber: 2, name: "Vashishth"});
    //dynamic array | we can specify fixed size in the braces []
    People[] public people;

    //mapping in solidity
    mapping(string => uint256) public nameTofavouriteNumber;


    function store(uint256 _favouriteNumber) public{
        favouriteNumber = _favouriteNumber;
    }

    function retrieve() public view returns(uint256){
        return favouriteNumber;
    }

    // memory-> only while execution | storage-> keep it forever
    function addPerson(string memory _name, uint256 _favouriteNumber) public{
        people.push(People(_favouriteNumber, _name));
        nameTofavouriteNumber[_name]= _favouriteNumber;
    }



}