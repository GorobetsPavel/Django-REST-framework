import React from "react";

const Footer = () => {
  return (
    <div class="row justify-content-center">
        <div bgColor='light' className='text-center text-lg-left'>
          <container className='p-4'>
            <div>
              <div lg='6' md='12' className='mb-4 mb-md-0'>
                <h5 className='text-uppercase'>Footer</h5>
                <ul class="list-unstyled">
                <li><a href="#">Положения &amp; Условия</a></li>
                <li><a href="#">Конфиденциальность &amp; Cookies</a></li>
                <li><a href="#">Документация по API</a></li>
                <li><a href="doc_site">Документация по сайту</a></li>
                </ul>
              </div>


            </div>
          </container>

          <div className='text-center p-3' style={{ backgroundColor: 'rgba(0, 0, 0, 0.2)' }}>
            &copy; {new Date().getFullYear()} Copyright:{' '}
            <a className='text-dark' href='#'>
              To DO
            </a>
          </div>
        </div>
    </div>
  );
};
export default Footer;