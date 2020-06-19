Vulnerable Contracts - 
ECEN-4133
In this part, you’ll investigate how to steal Ethereum from vulnerable smart contracts. We have
setup a vulnerable smart contract on the Ropsten testnet that you have permission to steal funds
from. However, using this technique on other contracts you do not have the same permission for
outside this class is a crime. Remember that just because you can do something technical, doesn’t
mean that you should!
We’ve deployed our contract to address 0xFB81aDf526904E3E71ca7C0d2dc841a94B1E203C. You
can download its source from https://ecen4133.org/static/vuln.sol.
The contract has two functions: deposit and withdraw that let you send and receive money from
the contract. On the surface, it appears that an address will only be able to withdraw what that
address originally deposited. But this contract is vulnerable to a bug that lets you extract more if
you’re clever!
In this part, you’ll write and use a contract that steals funds from the Vuln contract. Your goal is
to make a contract that includes a payable function, that interacts with the Vuln contract to steal
funds from it. Your contract should let you pay it a small amount (e.g. 0.1 ETH), and then later
let you extract a greater amount (e.g. 0.2 ETH). If we look at the (internal) transactions between
your contract and the Vuln contract, we should see that yours sends (deposits) less than it gets back
(withdraws) from the Vuln contract.
