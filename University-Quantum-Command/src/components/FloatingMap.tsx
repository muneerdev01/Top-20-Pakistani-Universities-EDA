"use client";

import React, { useEffect, useState } from 'react';
import dynamic from 'next/dynamic';
import { University } from './UniversityCard';
import 'leaflet/dist/leaflet.css';

// Dynamically import MapContainer and TileLayer to avoid SSR issues
const MapContainer = dynamic(() => import('react-leaflet').then(mod => mod.MapContainer), { ssr: false });
const TileLayer = dynamic(() => import('react-leaflet').then(mod => mod.TileLayer), { ssr: false });
const CircleMarker = dynamic(() => import('react-leaflet').then(mod => mod.CircleMarker), { ssr: false });
const Popup = dynamic(() => import('react-leaflet').then(mod => mod.Popup), { ssr: false });

// Simple static geocoding for Pakistani cities
const CITY_COORDS: Record<string, [number, number]> = {
    "Islamabad": [33.6844, 73.0479],
    "Lahore": [31.5204, 74.3587],
    "Karachi": [24.8607, 67.0011],
    "Peshawar": [34.0151, 71.5249],
    "Quetta": [30.1798, 66.9750],
    "Faisalabad": [31.4504, 73.1350],
    "Multan": [30.1575, 71.5249],
    "Jamshoro": [25.4225, 68.2825],
    "Topi": [34.0704, 72.6378], // GIKI
    "Bahawalpur": [29.3544, 71.6911],
};

// Fallback for unknown cities (Center of Pakistan)
const DEFAULT_COORD: [number, number] = [30.3753, 69.3451];

export default function FloatingMap({ universities }: { universities: University[] }) {
    const [isMounted, setIsMounted] = useState(false);

    useEffect(() => {
        setIsMounted(true);
    }, []);

    if (!isMounted) return <div className="h-[400px] w-full bg-[#050510] flex items-center justify-center text-cyan-500 animate-pulse">Initializing Geospatial Systems...</div>;

    return (
        <div className="h-full w-full relative z-0">
            <MapContainer
                center={DEFAULT_COORD}
                zoom={5}
                scrollWheelZoom={false}
                style={{ height: '100%', width: '100%', background: '#050510' }}
                attributionControl={false}
            >
                {/* Dark Matter Tiles */}
                <TileLayer
                    url="https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png"
                />

                {universities.map((uni, idx) => {
                    // Fuzzy match city from location string
                    const cityKey = Object.keys(CITY_COORDS).find(city => uni.Location.includes(city));
                    const coords = cityKey ? CITY_COORDS[cityKey] : DEFAULT_COORD;

                    // Add some jitter if multiple unis in same city
                    const jitterLat = coords[0] + (Math.random() - 0.5) * 0.05;
                    const jitterLng = coords[1] + (Math.random() - 0.5) * 0.05;

                    return (
                        <CircleMarker
                            key={idx}
                            center={[jitterLat, jitterLng]}
                            pathOptions={{
                                color: '#39FF14',
                                fillColor: '#39FF14',
                                fillOpacity: 0.6,
                                weight: 1
                            }}
                            radius={8}
                        >
                            <Popup className="glass-popup">
                                <div className="text-black font-bold">
                                    {uni["University Name"]}
                                    <br />
                                    <span className="text-xs font-normal">Score: {uni.Orbital_Stability}</span>
                                </div>
                            </Popup>
                        </CircleMarker>
                    );
                })}
            </MapContainer>
        </div>
    );
}
