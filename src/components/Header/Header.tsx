import React from "react";
import styles from "./Header.module.scss";
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

        <button className={styles.web3Button}>Connect Wallet</button>
      </nav>
    </header>
  );
};
