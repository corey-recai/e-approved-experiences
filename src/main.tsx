import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import { chain } from "wagmi";
import { Web3ModalProvider } from "@web3modal/react";
import { Web3ModalEthereum } from "@web3modal/ethereum";
import {
  avalanche,
  avalancheFuji,
  binanceSmartChain,
  binanceSmartChainTestnet,
  fantom,
  fantomTestnet,
} from "./chains";
import { NAMESPACE } from "./constants";

const customChains = [
  avalanche,
  avalancheFuji,
  binanceSmartChain,
  binanceSmartChainTestnet,
  fantom,
  fantomTestnet,
];

// const PROJECT_ID = process.env.WALLET_CONNECT_PROJECT_ID;
const PROJECT_ID = "d14659d55a7c0cf8badbf6b4f665aa3f";

import { jsonRpcProvider } from "@wagmi/core/providers/jsonRpc";
function walletConnectProvider({ projectId }) {
  return jsonRpcProvider({
    rpc: rpcChain => {
      const customChain = customChains.find(c => c.id === rpcChain.id);

      if (customChain)
        return {
          http: customChain.rpcUrls.default,
        };

      return {
        http: `https://rpc.walletconnect.com/v1/?chainId=${NAMESPACE}:${rpcChain.id}&projectId=${projectId}`,
      };
    },
  });
}

const config = {
  projectId: PROJECT_ID as string,
  theme: "dark" as "dark",
  accentColor: "default" as "default",
  ethereum: {
    appName: "approved-experieces",
    autoConnect: true,
    chains: [chain.mainnet],
    providers: [walletConnectProvider({ projectId: PROJECT_ID as string })],
  },
};

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
  <React.StrictMode>
    <Web3ModalProvider config={config} ethereumClient={config: config.ethereum}>
      <App />
    </Web3ModalProvider>
  </React.StrictMode>
);
