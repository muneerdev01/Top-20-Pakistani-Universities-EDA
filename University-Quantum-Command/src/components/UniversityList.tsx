"use client";

import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { Search } from 'lucide-react';
import UniversityCard, { University } from './UniversityCard';

export default function UniversityList({ universities }: { universities: University[] }) {
    const [searchTerm, setSearchTerm] = useState('');

    const filtered = universities.filter(u =>
        u["University Name"].toLowerCase().includes(searchTerm.toLowerCase()) ||
        u.Location.toLowerCase().includes(searchTerm.toLowerCase())
    );

    return (
        <div className="w-full">
            {/* Search Bar */}
            <div className="flex justify-center mb-12">
                <div className="relative w-full max-w-md">
                    <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                        <Search className="h-5 w-5 text-[#39FF14]" />
                    </div>
                    <input
                        type="text"
                        className="block w-full pl-10 pr-3 py-3 border border-white/10 rounded-full leading-5 bg-black/50 text-white placeholder-gray-400 focus:outline-none focus:bg-black/70 focus:ring-1 focus:ring-[#39FF14] focus:border-[#39FF14] sm:text-sm backdrop-blur-sm transition-all shadow-[0_0_15px_rgba(57,255,20,0.1)]"
                        placeholder="Search Quantum Coordinates (Name or City)..."
                        value={searchTerm}
                        onChange={(e) => setSearchTerm(e.target.value)}
                    />
                </div>
            </div>

            {/* Grid */}
            <motion.div
                layout
                className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8"
            >
                {filtered.map((uni) => (
                    <UniversityCard key={uni["University Name"]} uni={uni} />
                ))}
            </motion.div>

            {filtered.length === 0 && (
                <div className="text-center text-gray-500 mt-10">
                    No signals detected in this sector.
                </div>
            )}
        </div>
    );
}
