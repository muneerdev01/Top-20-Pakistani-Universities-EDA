import fs from 'fs';
import path from 'path';
import Papa from 'papaparse';
import { University } from '../components/UniversityCard';

export async function getUniversities(): Promise<University[]> {
    const filePath = path.join(process.cwd(), 'data', 'quantum_pak_universities.csv');

    try {
        const fileContent = fs.readFileSync(filePath, 'utf8');
        const { data } = Papa.parse(fileContent, {
            header: true,
            dynamicTyping: true,
            skipEmptyLines: true,
        });

        return data.map((row: any) => ({
            "University Name": row["University Name"],
            Location: row["Location"],
            Gravity_Resistance: Number(row["Gravity_Resistance"]) || 0,
            Orbital_Stability: Number(row["Orbital_Stability"]) || 0,
            Innovation_Thrust: Number(row["Innovation_Thrust"]) || 0,
            QS_Numeric: Number(row["QS_Numeric"]) || 700,
        })) as University[];
    } catch (error) {
        console.error("Failed to load quantum data:", error);
        return [];
    }
}
