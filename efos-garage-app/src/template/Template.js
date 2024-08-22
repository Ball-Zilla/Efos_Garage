import Header from './Header';
import Content from './Content';
import Footer from './Footer'; 

function Template({children}) {
  return (
    <div className="flex flex-col min-h-screen">
    <Header />
    <Content>{children}</Content>
    <Footer />
    </div>
  ) 
}

export default Template;