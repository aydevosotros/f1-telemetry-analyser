import React from 'react';
import styled from 'styled-components';
import SessionDataDisplay from '../components/SessionDataDisplay';
import { SessionData } from '../types';
import DashboardContent from '../components/DashboardContent';

const DashboardContainer = styled.div`
  display: flex;
  flex-direction: column;
  height: 100vh;
`;

const Header = styled.header`
  background-color: #4a4a4a;
  color: #fff;
  padding: 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.2);
  display: flex;
  align-items: center;
`;

const Tittle = styled.span`
  display: flex;
  margin-left: 20px; // add margin to push it over 
  font-size: 5em;
`;


const SessionSelector = styled.select`
  background: #fff;
  color: #333;
  padding: 5px 10px;
  border: none;
  border-radius: 4px;
`;

const SessionInfo = styled.div`
  background: #fff;
  color: #333;
  padding: 10px 20px;
  border-radius: 4px;
  margin-left: 20px;
`;

const MainContent = styled.main`
  display: flex;
  height: calc(100% - 64px); // subtract the header height
`;

const Sidebar = styled.aside`
  width: 200px;
  background-color: #f5f5f5;
  padding: 20px;
  box-shadow: 2px 0 4px 0 rgba(0, 0, 0, 0.2);
`;


const Dashboard = () => {

const sessionData: SessionData = {
    // Aquí puedes poner datos de prueba o reales
    m_weather: 0,
    m_trackTemperature: 20,
    m_airTemperature: 22,
    m_totalLaps: 50,
    m_trackLength: 5300,
    m_sessionType: 1,
    m_trackId: 5,
    m_formula: 0,
    m_sessionTimeLeft: 3600,
    m_sessionDuration: 7200,
    m_aiDifficulty: 80,
    m_pitStopWindowIdealLap: 25,
    m_pitStopWindowLatestLap: 30,
    m_pitStopRejoinPosition: 3,
    m_timeOfDay: 780,
    };

  return (
    <DashboardContainer>
      <Header>
        <SessionSelector>
          <option value="1">Sesión 1</option>
          <option value="2">Sesión 2</option>
          {/* Puedes añadir más opciones aquí */}
        </SessionSelector>
        <Tittle>F1 23 Analyzer</Tittle>
        <SessionDataDisplay  data={sessionData}/>
      </Header>
      
      <MainContent>
        <Sidebar>
          {/* Aquí puedes añadir elementos de menú */}
          <a>Real-Time</a>
        </Sidebar>
        <DashboardContent>
          {/* Aquí puedes añadir el contenido de tu dashboard */}
          Contenido del dashboard
        </DashboardContent>
      </MainContent>
    </DashboardContainer>
  );
};

export default Dashboard;
