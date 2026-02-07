import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import './globals.css';

const inter = Inter({ subsets: ['latin'] });

export const metadata: Metadata = {
    title: 'Quantum Command | Smart Edu-Gravity',
    description: 'Anti-Gravity University Rankings - Pakistan Sector',
};

export default function RootLayout({
    children,
}: {
    children: React.ReactNode;
}) {
    return (
        <html lang="en">
            <body className={`${inter.className} bg-[#050510] text-white`}>{children}</body>
        </html>
    );
}
