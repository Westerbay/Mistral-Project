const serverAddr = "172.232.36.114";
const serverPort = 5555;

$(document).ready(() => {
    const userInterface = new UserInterface(serverAddr, serverPort);
    userInterface.addEventListeners();
});
