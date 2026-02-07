"use client";

import { motion } from "framer-motion";
import { Zap, Activity, Rocket, MapPin } from "lucide-react";
import React from "react";

// Define the shape of our University data
export interface University {
    "University Name": string;
    Location: string;
    Gravity_Resistance: number;
    Orbital_Stability: number;
    Innovation_Thrust: number;
    QS_Numeric: number;
}

export default function UniversityCard({ uni }: { uni: University }) {
    // Normalize metrics for visual bars (approximate max values)
    const gravityPercent = Math.min(uni.Gravity_Resistance * 10, 100); // e.g. 7.2 -> 72%
    const stabilityPercent = (uni.Orbital_Stability / 700) * 100;
    const thrustPercent = Math.min(uni.Innovation_Thrust * 10, 100);

    return (
        <motion.div
            initial={{ y: 0, opacity: 0 }}
            animate={{
                y: [0, -8, 0],
                opacity: 1
            }}
            transition={{
                y: {
                    duration: 6,
                    repeat: Infinity,
                    ease: "easeInOut"
                },
                opacity: { duration: 0.5 }
            }}
            className="group relative p-6 rounded-2xl border border-white/10 bg-black/40 backdrop-blur-md shadow-[0_0_0_1px_rgba(255,255,255,0.05)] hover:shadow-[0_0_30px_rgba(57,255,20,0.2)] transition-all duration-500 overflow-hidden hover:border-[#39FF14]/50"
        >
            {/* Neon Glow Gradient */}
            <div className="absolute -inset-1 bg-gradient-to-r from-[#39FF14] to-cyan-500 rounded-2xl opacity-0 group-hover:opacity-20 blur-xl transition-opacity duration-500" />

            {/* Content */}
            <div className="relative z-10 flex flex-col h-full">
                <div className="flex justify-between items-start mb-4">
                    <h3 className="text-xl font-bold text-white leading-tight group-hover:text-[#39FF14] transition-colors">
                        {uni["University Name"]}
                    </h3>
                    <div className="px-2 py-1 rounded bg-white/10 text-xs text-cyan-300 font-mono border border-cyan-500/30">
                        R-{700 - uni.Orbital_Stability}
                    </div>
                </div>

                <p className="text-sm text-gray-400 mb-6 flex items-center gap-1.5">
                    <MapPin size={14} className="text-[#39FF14]" />
                    {uni.Location}
                </p>

                {/* Quantum Metrics */}
                <div className="space-y-4 mt-auto">
                    {/* Gravity Resistance */}
                    <div className="space-y-1">
                        <div className="flex justify-between text-xs uppercase tracking-wider">
                            <span className="flex items-center gap-1 text-cyan-400"><Activity size={12} /> Gravity Res.</span>
                            <span className="font-mono text-cyan-200">{uni.Gravity_Resistance.toFixed(1)}%</span>
                        </div>
                        <div className="h-1 bg-white/10 rounded-full overflow-hidden">
                            <motion.div
                                initial={{ width: 0 }}
                                animate={{ width: `${gravityPercent}%` }}
                                transition={{ duration: 1, delay: 0.2 }}
                                className="h-full bg-cyan-500 shadow-[0_0_8px_cyan]"
                            />
                        </div>
                    </div>

                    {/* Orbital Stability */}
                    <div className="space-y-1">
                        <div className="flex justify-between text-xs uppercase tracking-wider">
                            <span className="flex items-center gap-1 text-[#39FF14]"><Zap size={12} /> Orb. Stability</span>
                            <span className="font-mono text-[#39FF14]">{uni.Orbital_Stability}</span>
                        </div>
                        <div className="h-1 bg-white/10 rounded-full overflow-hidden">
                            <motion.div
                                initial={{ width: 0 }}
                                animate={{ width: `${stabilityPercent}%` }}
                                transition={{ duration: 1, delay: 0.4 }}
                                className="h-full bg-[#39FF14] shadow-[0_0_8px_#39FF14]"
                            />
                        </div>
                    </div>

                    {/* Innovation Thrust */}
                    <div className="space-y-1">
                        <div className="flex justify-between text-xs uppercase tracking-wider">
                            <span className="flex items-center gap-1 text-purple-400"><Rocket size={12} /> Thrust</span>
                            <span className="font-mono text-purple-200">{uni.Innovation_Thrust}</span>
                        </div>
                        <div className="h-1 bg-white/10 rounded-full overflow-hidden">
                            <motion.div
                                initial={{ width: 0 }}
                                animate={{ width: `${thrustPercent}%` }}
                                transition={{ duration: 1, delay: 0.6 }}
                                className="h-full bg-purple-500 shadow-[0_0_8px_purple]"
                            />
                        </div>
                    </div>
                </div>
            </div>
        </motion.div>
    );
}
