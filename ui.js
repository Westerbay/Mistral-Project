class UserInterface {

    constructor(serverAddr, serverPort) {
        this.chatBox = $("#chat-box");
        this.chatForm = $("#chat-form");
        this.userInput = $("#user-input");
        this.modelSelector = $("#modelSelector");
        this.submitButton = this.chatForm.find("button");
        this.serverAddr = serverAddr;
        this.serverPort = serverPort;
        this.request("get_models", this.saveModels.bind(this));
    }

    addEventListeners() {
        this.chatForm.submit((event) => {
            event.preventDefault();
            this.sendUserPrompt();      
            this.autoResizeUserInput();    
        });
        this.userInput.on("input", () => {
            this.autoResizeUserInput();
        });
        this.userInput.keypress((event) => {
            if (event.which === 13 && !event.shiftKey) {  
                event.preventDefault();
                this.chatForm.submit();
            }
        });
        this.modelSelector.on("change", (event) => {
            const selectedValue = $(event.target).val();
            this.model = selectedValue;
            this.changeModel();
        });
    }

    changeModel() {
        // First Clear the chat 
        this.chatBox.html("");

        //Asking its role
        const prompt = "I let you introduce shortly your role in 30 words maximum in one paragraph.";
        this.sendPrompt(prompt);
    }

    sendPrompt(prompt) {
        // Disable submit button
        this.submitButton.prop("disabled", true);  
        const data = JSON.stringify({
            prompt : prompt,
            model : this.model
        });

        //Request
        this.thinkingBubble = $(`<div class="ai thinking">...</div>`);
        this.chatBox.append(this.thinkingBubble);
        this.request("request", this.promptSuccess.bind(this), data);
    }

    sendUserPrompt() {
        const userMessage = this.userInput.val();        
        const userChatBox = `<div class="user">${userMessage}</div>`;
        this.chatBox.append(userChatBox);
        this.userInput.val("");      
        this.sendPrompt(userMessage);
        this.scrollToBottom();
    }

    request(route, success, data=null) {
        $.ajax({
            url: `http://${this.serverAddr}:${this.serverPort}/${route}`,
            type: "POST",
            contentType: "application/json",
            data: data,
            success: success,
            error: this.requestError.bind(this)
        });
    }

    saveModels(response) {
        this.models = response.models;
        for (var model of this.models) {
            this.modelSelector.append(
                $("<option>", {
                    value: model,
                    text: `Model : ${model}`
                })
            );
        }
        this.model = this.models[0];
        this.modelSelector.val(this.models[0]);
        this.changeModel(this.models[0]);
    }

    promptSuccess(response) {
        const html = marked.parse(response.text);
        const aiChatBox = `<div class="ai">${html}</div>`;
        this.chatBox.append(aiChatBox);
        this.requestEnd();
    }

    requestError(xhr) {
        const errorMessage = `<div class="error">Error: status ${xhr.status}, ${xhr.statusText}</p>`;
        this.chatBox.append(errorMessage);
        this.requestEnd();
    }

    requestEnd() {
        if (this.thinkingBubble) {
            this.thinkingBubble.remove();
            this.thinkingBubble = null;
        }
        this.submitButton.prop("disabled", false);
    }

    scrollToBottom() {
        const chatBox = this.chatBox[0];
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    autoResizeUserInput() {
        const el = this.userInput[0];
        el.style.height = "52px";
        el.style.height = Math.min(el.scrollHeight, 200) + "px";
    }

};
