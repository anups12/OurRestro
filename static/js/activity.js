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
        showNotification()
    }
}

function showNotification(){
    const notification = new Notification(` Hey ${user} Hope you are good`, {
        body:`Hello ${user} you are inactive for more than 5 minutes`
    });
    notification.onclick = (e)=>{
        window.location.href='/'
    }
}

if (user !== 'AnonymousUser'){
    if(Notification.permission !== "denied" || Notification.permission==='default'){
        Notification.requestPermission().then(permission=>{
            if(permission==='granted'){
                resetTimer()
            }
        })
    }
}
