import React, { useEffect, useRef } from "react";
import styles from "./Hero.module.scss";

interface Props {
  title: string;
}

export const Hero: React.FC<Props> = ({ title }) => {
  return (
    <div className={styles.hero}>
      <div className={styles.videoContainer}>
        <video
          src='https://video.wixstatic.com/video/6da91d_1cf23ceb66ae4b758c05b25b290d5a52/1080p/mp4/file.mp4'
          autoPlay
          playsInline
          muted
          loop
        />
        <div className={styles.overlay} />
      </div>
      <div className={styles.title}>
        <h1>{title}</h1>
      </div>
    </div>
  );
};
