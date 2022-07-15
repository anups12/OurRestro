let timer, currSeconds = 0;

function resetTimer() {

    /* Hide the timer text */
    document.querySelector(".timertext")
        .style.display = 'none';

    /* Clear the previous interval */
    clearInterval(timer);

    /* Reset the seconds of the timer */
    currSeconds = 0;

    /* Set a new interval */
    timer =
        setInterval(startIdleTimer, 1000);
}

// Define the events that
// would reset the timer
window.onload = resetTimer;
window.onmousemove = resetTimer;
window.onmousedown = resetTimer;
window.ontouchstart = resetTimer;
window.onclick = resetTimer;
window.onkeypress = resetTimer;

function startIdleTimer() {

    /* Increment the
        timer seconds */
    currSeconds++;
    if(currSeconds==300){
        NotifyUser(user)
    }
}


function NotifyUser(user) {
    var url = '/message/'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({ 'user': user})
    })
        .then((response) => {
            return response.json()
        }).then((data) => {
            console.log(data);
        })

}