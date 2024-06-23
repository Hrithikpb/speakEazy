import "../styles/globals.css";
import "@fontsource/poppins";
import "@fontsource/poppins/300.css";
import "@fontsource/poppins/400.css";
import "@fontsource/poppins/500.css";
import "@fontsource/poppins/600.css";

import type { AppProps } from "next/app";
import Head from "next/head";
import { Nav } from "../components/menu/Nav";
import { Toolbar } from "../components/menu/Toolbar";

export default function App({ Component, pageProps }: AppProps) {
  return (
    <>
      <Head>
        <title>SpeakEazy</title>
        <meta name="title" content="Speakeazy" />
        <meta name="description" content="Learn to speak easily." />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <div className="min-w-screen min-h-screen bg-neutral-100 font-main font-thin text-neutral-800">
        <> 
          <Nav />
          <>
            <div>
              <Component {...pageProps} />
            </div>
          </>
        </>
      </div>
    </>
  );
}
