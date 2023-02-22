// ===================================== AUTO ORDERING - FUNCTIONALITY ===================================== //
var my_heading = $(".myDiv h4");
for (var l = 0; l < my_heading.length; l++) {
    var currect_text = my_heading[l].textContent;
    my_heading[l].textContent = (l + 1) +". " + currect_text;
}


// ===================================== MARK ANSWER - FUNCTIONALITY ===================================== //
$(".buttonDiv button").click(function() {
    fillButton(this);
})

function fillButton(control) {
    // un-fill another button:
    $(control).parent().parent().children().children().css("background-color", "transparent");
    $(control).parent().parent().children().children().css("color", "black");
    // fill pressed button:
    $(control).css("background-color", "#303861");
    $(control).css("color", "white");
}

// ===================================== CHECK ANSWER - FUNCTIONALITY ===================================== //
$(".submit").click(function() {
    // hold correct answers:
    var correct_inputs = $(".hold_correct");
    var correct_answers = [];
    for (var i = 0; i < correct_inputs.length; i++) {
        correct_answers.push(correct_inputs[i].value);
    }

    // hold pressed buttons:
    var all_buttons = $(".buttonDiv button");
    var pressed_buttons = [];
    var blue_buttons = []
    for (var j = 0; j < all_buttons.length; j++) {
        if (all_buttons[j].style.backgroundColor != "transparent") {
            pressed_buttons.push(all_buttons[j].textContent);
            blue_buttons.push(all_buttons[j]);
        }
    }

    // count final score:
    var final_score = 0;
    if (correct_answers.length == pressed_buttons.length) {
        for (var k = 0; k < correct_answers.length; k++) {
            if (correct_answers[k] == pressed_buttons[k]) {
                final_score++;
            }
        }
    }

    // red background for wrong answers:
    for (var r = 0; r < blue_buttons.length; r++) {
        if (blue_buttons[r].textContent != correct_answers[r]) {
            blue_buttons[r].style.backgroundColor = "red";
        }
        else {
            blue_buttons[r].style.backgroundColor = "green";
        }
    }

    // light green for unchecked - right answers:
    var answer_placeholders = $("h6");
    for (var h = 0; h < answer_placeholders.length; h++) {
        answer_placeholders[h].style.display = "block";
        $(answer_placeholders[h]).children("span").text(correct_answers[h]);
    }

    // show final result:
    $(".finalScore").css("display", "block");
    $(".finalScore").text("Final Score: " + final_score + " / " + correct_answers.length);

})