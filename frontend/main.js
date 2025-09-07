const serverAddr = "localhost";
const serverPort = 8000;

$(document).ready(() => {
    const userInterface = new UserInterface(serverAddr, serverPort);
    userInterface.addEventListeners();
});
