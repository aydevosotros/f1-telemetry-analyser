import React from 'react';
import Layout from '../components/Layout';
import SessionDataDisplay from '../components/SessionDataDisplay';
import { SessionData } from '../types';
import styled from 'styled-components';

const StyledHeader = styled.h2`
  color: #333;
  font-size: 24px;
  text-align: center;
`;

const StyledDataDisplay = styled(SessionDataDisplay)`
  background-color: #fafafa;
  border-radius: 8px;
  padding: 16px;
  margin-top: 16px;
`;

const TestPage: React.FC = () => {
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
    <Layout>
      <StyledHeader>Esta es la página de prueba</StyledHeader>
      <StyledDataDisplay data={sessionData} />
    </Layout>
  );
};

export default TestPage;