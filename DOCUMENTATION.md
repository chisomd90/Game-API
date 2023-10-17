## Game WebSocket Service Documentation

### Introduction

Welcome to the WebSocket service for our multiplayer game platform. This service allows game developers to implement real-time, WebSocket-based communication for their multiplayer games. In this documentation, you'll find information on how to connect to our WebSocket service, the WebSocket URL format, and common use cases.

### WebSocket URL Format

To connect to the WebSocket service for your game, use the following URL format:
```
ws://stone-4asd.onrender.com/ws/game/<game_id>/
# ws: This is the WebSocket protocol identifier.
```
ws/game/<game_id>/: This part of the URL should be customized according to your game's configuration. Replace <game_id> with the specific game's ID or identifier you want to connect to.

### Authentication

Depending on the security and authentication requirements of your game, you may need to include additional authentication headers, tokens, or API keys when connecting to the WebSocket service. Be sure to check our specific authentication requirements if any.

### Connecting to the WebSocket Service

To connect to the WebSocket service, you can use WebSocket client libraries for your preferred programming language. Below are some examples of how to establish a WebSocket connection in different languages:

JavaScript

```
const gameWebSocket = new WebSocket('ws://stone-4asd.onrender.com/ws/game/<game_id>/');

gameWebSocket.addEventListener('open', (event) => {
    // Connection is open
});

gameWebSocket.addEventListener('message', (event) => {
    // Handle incoming messages from the game
});

gameWebSocket.addEventListener('close', (event) => {
    // Connection is closed
});
```

### Sending and Receiving Messages

Once connected, you can send and receive messages related to your game's functionality, such as player movements, game state updates, or chat messages. Messages should be serialized to JSON for easy communication.

SEnding a message
```
const message = {
    type: 'player_movement',
    data: { x: 100, y: 200 }
};

gameWebSocket.send(JSON.stringify(message));
```

Receiving a message
```
gameWebSocket.addEventListener('message', (event) => {
    const message = JSON.parse(event.data);
    // Handle the received message
});
```