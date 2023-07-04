import React from 'react';
import { SessionData } from './types'; // Asegúrate de que la ruta es correcta

function secondsToHms(seconds: number) {
    seconds = Number(seconds);
    const h = Math.floor(seconds / 3600);
    const m = Math.floor(seconds % 3600 / 60);
    const s = Math.floor(seconds % 3600 % 60);
  
    const hDisplay = h > 0 ? h + (h === 1 ? " hora, " : " horas, ") : "0";
    const mDisplay = m > 0 ? m + (m === 1 ? " minuto, " : " minutos, ") : "0";
    const sDisplay = s > 0 ? s + (s === 1 ? " segundo" : " segundos") : "0";
    return hDisplay + mDisplay + sDisplay; 
  }

const SessionDataDisplay: React.FC<{ data: SessionData }> = ({ data }) => (
  <div>
    <p>Tiempo restante de la sesión: {secondsToHms(data.m_sessionTimeLeft)} segundos</p>
    <p>Duración total de la sesión: {secondsToHms(data.m_sessionDuration)} segundos</p>
    <p>Temperatura de la pista: {data.m_trackTemperature} grados Celsius</p>
  </div>
);

export default SessionDataDisplay;