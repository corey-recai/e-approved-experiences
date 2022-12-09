import React, { useEffect, useRef } from "react";
import styles from "./Hero.module.scss";

interface Props {
  title: string;
  media: {
    type: "image" | "video";
    link: string;
  };
}

export const Hero: React.FC<Props> = ({ title, media }) => {
  return (
    <div className={styles.hero}>
      <div className={styles.videoContainer}>
        {media.type === "video" && (
          <video src={media.link} autoPlay playsInline muted loop />
        )}
        {media.type === "image" && <img src={media.link} alt={title} />}
        <div className={styles.overlay} />
      </div>
      <div className={styles.title}>
        <h1>{title}</h1>
      </div>
    </div>
  );
};
