import React from "react";
import { Grid } from "../../components/Grid";
import { Hero } from "../../components/Hero";
import { Header } from "../../components/Header";

export const ExoticCars: React.FC = () => {
  return (
    <>
      <Header />
      <main>
        <Hero title='Miami Exotic Car Rentals' />
        <Grid />
      </main>
    </>
  );
};
