$(document).on('ready', main);

function main(){
    $('.close_message').on('click', fadeMessage);
}

function fadeMessage() {
    $('#messages_section').fadeOut("slow");
}
