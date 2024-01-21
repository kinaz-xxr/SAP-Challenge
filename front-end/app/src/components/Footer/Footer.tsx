import React from 'react';
import { MDBFooter } from 'mdb-react-ui-kit';
import styles from "./Footer.module.scss";

export default function App() {
  return (
    <MDBFooter bgColor='light' className='text-center text-lg-left'>
      <div className='text-center p-3 margin-top' style={{ backgroundColor: 'rgba(0, 0, 0, 0.2)' }}>
        &copy; {new Date().getFullYear()} Copyright:{' '}
        <a className='text-dark' href='https://mdbootstrap.com/'>
          Quang Bui, Kent Tran, DB Nguyen, Dat Bui
        </a>
      </div>
    </MDBFooter>
  );
}
