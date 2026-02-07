import { getUniversities } from '../lib/universities';
import UniversityList from '../components/UniversityList';
import FloatingMap from '../components/FloatingMap';
import { Rocket } from 'lucide-react';

export default async function Home() {
    const universities = await getUniversities();

    return (
        <main className="min-h-screen bg-[#050510] relative overflow-hidden text-white selection:bg-[#39FF14] selection:text-black">
            <div className="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-20 pointer-events-none"></div>

            <div className="relative z-10 container mx-auto px-4 py-12 text-center">
                <h1 className="text-6xl font-bold mb-4 tracking-tighter text-transparent bg-clip-text bg-gradient-to-r from-white via-cyan-200 to-[#39FF14] drop-shadow-[0_0_15px_rgba(57,255,20,0.5)]">
                    QUANTUM COMMAND
                </h1>
                <p className="text-xl text-cyan-400/80 mb-8 max-w-2xl mx-auto flex items-center justify-center gap-2">
                    <Rocket size={20} />
                    My First Dataset "University Rankings • Pakistan Sector"
                </p>

                {/* Map Section */}
                <div className="h-[400px] w-full rounded-2xl overflow-hidden border border-white/10 mb-12 relative shadow-[0_0_50px_rgba(0,0,0,0.5)]">
                    <FloatingMap universities={universities} />
                </div>

                <UniversityList universities={universities} />
            </div>

            <footer className="relative z-10 text-center py-8 text-white/20 text-xs uppercase tracking-widest border-t border-white/5 mt-20">
                System Status: Operational • Gravity Normalization Active
            </footer>
        </main>
    );
}
