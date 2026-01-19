import './Header.css';
import logo from "../../assets/images/logo.png";
import logoutIcon from "../../assets/icons/logout.png";
import { useNavigate } from "react-router-dom";

export default function Header(props){

    const navigate = useNavigate();

    const handleLogout = () => {
        localStorage.removeItem("usuarioLogado");
        navigate("/"); 
    };

    return(
        <div className="header">
            <div onClick={() => navigate("/dashboard")}>
                <img src={logo} alt="Logo do SIFRA" className="responsive-img"/>
            </div>
            <div className="user" style={{display: `${props.display}`}}>
                <p>{props.username}</p>
                <img className='logout-icon' src={logoutIcon} alt='Sair' title='Sair' onClick={handleLogout}/>
            </div>
        </div>
    );
}
