import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";

// const PROJECT_ID = process.env.WALLET_CONNECT_PROJECT_ID;
const PROJECT_ID = "d14659d55a7c0cf8badbf6b4f665aa3f";

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
