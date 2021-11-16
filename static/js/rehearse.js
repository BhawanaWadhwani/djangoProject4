var visibleCard = 0;
var cardSide = "QuestionSide";

// this will show flash cards to be rehearsed by loading the deck first
// from the DB and subsequenly iterating through them. Default: show Question,
// hide Answer
function showCard(){
  $(".rehearse_card").hide();
  $(".card-title-question").hide();
  $(".card-text-answer").hide();
  $(".rehearse_card:eq(" + visibleCard + ")").show();
  $(".card-title-question").show();
}


// this toggles which side of the flashcard to be shown, i.e. question or answer
function flipCard(){
  if(cardSide == "QuestionSide"){
      cardSide = "AnswerSide";
      $(".card-title-question").hide();
      $(".card-text-answer").show();
      console.log("show Q")
  }else{
      $(".card-title-question").show();
      $(".card-text-answer").hide();
      console.log("show A");
      cardSide = "QuestionSide"
      }
  }


// below functions allow cycling back and forth through the chosen flashcard deck
function showNextCard(){
  if(visibleCard == $(".rehearse_card").length-1){
    visibleCard = 0;
  }else{
    visibleCard++;
  }
  showCard();
}


function showPrevCard(){
  if (visibleCard == 0){
    visibleCard = $(".rehearse_card").length-1;
  }else{
    visibleCard--;
  }
  showCard();
}


showCard();
