import React, { useEffect, useState } from "react";
import SignClient from "@walletconnect/sign-client";
import { Web3Modal } from "@web3modal/standalone";

import styles from "./Header.module.scss";

const web3modal = new Web3Modal({
  projectId: "d14659d55a7c0cf8badbf6b4f665aa3f",
});

const navItems = [
  { name: "Exotic Cars", path: "exotic-cars" },
  { name: "Luxury Yachts", path: "luxury-yachts" },
  { name: "Luxury Villas", path: "luxury-villas" },
  { name: "Private Jets", path: "private-jets" },
  { name: "Other Services", path: "other-services" },
  { name: "About Us", path: "about-us" },
  { name: "Contact Us", path: "contact-us" },
];
export const Header: React.FC = () => {
  const [signClient, setSignClient] = useState<SignClient | undefined>(
    undefined
  );

  // 3. Initialize sign client
  async function onInitializeSignClient() {
    const client = await SignClient.init({
      projectId: "d14659d55a7c0cf8badbf6b4f665aa3f",
    });
    setSignClient(client);
  }

  // 4. Initiate connection and pass pairing uri to the modal
  async function onOpenModal() {
    if (signClient) {
      const namespaces = {
        eip155: {
          methods: ["eth_sign"],
          chains: ["eip155:1"],
          events: ["accountsChanged"],
        },
      };
      const { uri, approval } = await signClient.connect({
        requiredNamespaces: namespaces,
      });
      if (uri) {
        web3modal.openModal({
          uri,
          standaloneChains: namespaces.eip155.chains,
        });
        await approval();
        web3modal.closeModal();
      }
    }
  }

  useEffect(() => {
    onInitializeSignClient();
  }, []);

  return (
    <header className={styles.header}>
      <nav className={styles.nav}>
        <img
          src='https://static.wixstatic.com/media/6da91d_db58c263e28448e4ac60ba7f528a110f~mv2.png/v1/fill/w_244,h_104,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/6da91d_db58c263e28448e4ac60ba7f528a110f~mv2.png'
          alt='Logo.'
        />
        <ul className={styles.navList}>
          {navItems.map(item => {
            return <li key={item.path}>{item.name} </li>;
          })}
        </ul>

        <button className={styles.web3Button} onClick={onOpenModal}>
          {signClient ? "Connect Wallet" : "Initializing..."}
        </button>
      </nav>
    </header>
  );
};
