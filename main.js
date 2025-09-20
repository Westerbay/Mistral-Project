const serverAddr = "wester.games";
const serverPort = 5555;

$(document).ready(() => {
    const userInterface = new UserInterface(serverAddr, serverPort);
    userInterface.addEventListeners();
});
