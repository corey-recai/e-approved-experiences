import React from "react";
import styles from "./Header.module.scss";
import { useEthers, useEtherBalance } from "@usedapp/core";

// Regular import crashes the app with "Buffer is not defined" error.
import WalletConnectProvider from "@walletconnect/web3-provider";

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
  const { account, activate, deactivate, chainId } = useEthers();
  const etherBalance = useEtherBalance(account);
  // if (!config.readOnlyUrls[chainId]) {
  //   return <p>Please use either Mainnet or Goerli testnet.</p>;
  // }

  // async function onConnect() {
  //   try {
  //     const provider = new WalletConnectProvider({
  //       infuraId: "d8df2cb7844e4a54ab0a782f608749dd",
  //     });
  //     await provider.enable();
  //     await activate(provider);
  //   } catch (error) {
  //     console.error(error);
  //   }
  // }
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

        <button
          className={styles.web3Button}
          // onClick={onConnect}
        >
          Connect Wallet
        </button>
      </nav>
    </header>
  );
};
