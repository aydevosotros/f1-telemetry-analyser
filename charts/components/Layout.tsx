import React from 'react';

const Layout: React.FC = ({ children }) => (
  <div>
    <header>
      <h1>Título de la aplicación</h1>
      {/* Aquí puedes añadir tu menú de navegación, logo, etc. */}
    </header>

    <main>
      {children}
      {/* Los componentes hijos pasados al Layout se renderizarán aquí. */}
    </main>

    <footer>
      <p>Este es el pie de página</p>
    </footer>
  </div>
);

export default Layout;