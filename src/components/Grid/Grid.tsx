import React from "react";
import listings from "../../data/data.json";
import styles from "./Grid.module.scss";

export const Grid = () => {
  return (
    <div className={styles.grid}>
      {listings.data.catalog.category.productsWithMetaData.list.map(product => {
        return (
          <div className={styles.card} key={product.id}>
            <div className={styles.image}>
              <img
                src={`https://static.wixstatic.com/media/${product.media[0].url}/v1/fill/w_538,h_359,al_c,q_80,usm_0.66_1.00_0.01/${product.media[0].url}.replace(/\.[^.]*$/,'.webp')`}
              />
            </div>
            <div className={styles.description}>
              <div>
                <span>{product.name}</span>
              </div>
              <div className={styles.price}>
                <span>{product.formattedPrice} per day</span>
              </div>
            </div>
          </div>
        );
      })}
    </div>
  );
};
