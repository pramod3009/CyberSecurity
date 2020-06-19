pragma solidity ^0.5.0;
contract rps{
    
    mapping (string => mapping(string => int)) decide_winner;
    int public winner;
    string private player1_choice;
    string private player2_choice;
    
    constructor() public{
        decide_winner["rock"]["rock"] = 3;
        decide_winner["rock"]["paper"] = 2;
        decide_winner["rock"]["scissors"] = 1;
        decide_winner["paper"]["rock"] = 1;
        decide_winner["paper"]["paper"] = 3;
        decide_winner["paper"]["scissors"] = 2;
        decide_winner["scissors"]["rock"] = 2;
        decide_winner["scissors"]["paper"] = 1;
        decide_winner["scissors"]["scissors"] = 3;
        winner = 0;
    }
    address payable private player1;
    address payable private player2;
    
    bytes32 private player1_commitment;
    bytes32 private player2_commitment;
    uint256 private player1_wager;
    uint256 private player2_wager;
    bool private player1_played;
    bool private player2_played;
    
    
    function encode_commitment(string memory choice, string memory rand)
        public pure returns (bytes32) { 
            return sha256(abi.encodePacked(choice, rand));
        }
        
        function play(bytes32 commitment) public payable { 
            if(player1==address(0)){
                player1 = msg.sender;
                player1_wager = msg.value;
                player1_commitment = commitment;
            } else if(player2==address(0)){
                player2 = msg.sender;
                if(msg.value < player1_wager){
                    revert("invalid wager");//revert
                } else if (msg.value > player1_wager){
                    player2.transfer(msg.value - player1_wager);
                    player2_commitment = commitment;
                    player2_wager = msg.value - player1_wager;
                    
                } else {
                    player2_commitment = commitment;
                    player2_wager = msg.value;
                }
                
            }
        }
        
        function reveal(string memory choice, string memory rand) public { 
            if(msg.sender == player1 || msg.sender == player2) {
                
                if(msg.sender == player1 && sha256(abi.encodePacked(choice, rand)) == player1_commitment) {
                    player1_played = true;
                    player1_choice = choice;
                }
                
                if(msg.sender == player2 && sha256(abi.encodePacked(choice, rand)) == player2_commitment){
                    player2_played = true;
                    player2_choice = choice;
                }
                
                if(player1_played && player2_played){
                   winner = decide_winner[player1_choice][player2_choice];
                }
            } else {
                revert("invalid player-full house");
            }
            
        }
        
        function withdraw() public {
            if(winner==0){
                revert("winner has not been decided yet waiting for other player");
            }
            if(winner==1){
                player1.transfer(address(this).balance);
            } else if(winner==2){
                player2.transfer(address(this).balance);
            } else{
                player1.transfer(address(this).balance/2);
                player2.transfer(address(this).balance);
            }
            
            //reset
            winner = 0;
            
            player1 = address(0);
            player1_commitment = bytes32(0);
            player1_wager = uint256(0);
            player1_choice = "";
            player1_played = false;
            
            player2 = address(0);
            player2_commitment = bytes32(0);
            player2_wager = uint256(0);
            player2_choice = "";
            player2_played = false;
        }
        
}