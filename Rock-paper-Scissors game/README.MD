The game works as follows:
1. Player one submits a wager with a certain amount of Ethereum to the contract, and a blinded
commitment of their choice (“rock”, “paper”, or “scissors”). This is done by calling the
play() function with funds and a commitment (formed by calling the encode_commitment()
function).
2. Player two submits an equal wager (if greater, the excess should be refunded, if less, the
wager is invalid), and their commitment (rock/paper/scissors) by calling play().
3. Each player then submits a transaction that unblinds their commitment by calling reveal(),
which reveals to the contract (and the world) what their original rock/paper/scissors choice
was.
4. Once both commitments are revelead (i.e. both players have called reveal() with valid
arguments), the contract should determine the winner, and the winner should be allowed to
claim the wagers from both players, with the loser getting nothing. In the event of a tie, the
players should be allowed to reclaim their own wager.
