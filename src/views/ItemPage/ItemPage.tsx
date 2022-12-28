import React from "react";
import { Grid } from "../../components/Grid";
import { Hero } from "../../components/Hero";
import { Layout } from "../../components/Layout";

interface Props {
  title: string;
  media: {
    type: "image" | "video";
    link: string;
  };
  data: any;
}

export const ItemPage = ({ title, media, data }: Props) => {
  return (
    <Layout>
      <Hero title={title} media={media} />
      <Grid {...data} />
    </Layout>
  );
};
