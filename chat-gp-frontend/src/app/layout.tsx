import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import Navbar from "./Navbar";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "ChatGP",
  description: "Chat with a GP",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={inter.className + "bg-slate-200 p-0"}>
        <div className="absolute w-full h-full bg-slate-200 -z-10"></div>
        <Navbar />
        {children}
      </body>
    </html>
  );
}
