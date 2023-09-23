let selectOption='';
let result='';
let count=0;
let score={
    win:0,
    lose:0
}


function computerSelection(){
    const randomNum=Math.random();
    if(randomNum>0 && randomNum< 1/2){
        selectionOption='head';
    }
    else if(randomNum> 1/2 && randomNum < 1){
        selectionOption='tail';
    }
    return selectionOption;
}


function playGame(computer,you){
    if(computer==='head' && you==='head'){
        result="You win";
        score.win+=1;
        count++;
    }
    else if(computer==='head' && you==='tail'){
        result='You lose';
        score.lose+=1;
        count++;
    }
    else if(computer==='tail' && you==='tail'){
        result="You win";
        score.win+=1;
        count++;
    }
    else if(computer==='tail' && you==='head'){
        result="You lose";
        score.lose+=1;
        count++;
    }
    alert(`You picked ${you}, computer picked ${computer},${result}
You: ${score.win}  computer: ${score.lose}`)
   
   if(count=== 10){
      if(score.win > score.lose){
        alert("Congrats You win!");  
      }
      else{
        alert("Sorry You Lose!");
        score={
            win:0,
            lose:0
        }
      }
   }
  
}
