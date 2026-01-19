import './Header.css';
import logo from "../../assets/images/logo.png";
import userPlaceholder from "../../assets/images/user.png";
import logoutIcon from "../../assets/icons/logout_icon.png";
import { useEffect, useRef, useState } from "react";
import { useNavigate } from "react-router-dom";

export default function Header(props){

    const navigate = useNavigate();
    const [isMenuOpen, setIsMenuOpen] = useState(false);
    const userMenuRef = useRef(null);

    const handleLogout = () => {
        localStorage.removeItem("usuarioLogado");
        navigate("/"); 
    };

    const toggleMenu = () => {
        setIsMenuOpen((prev) => !prev);
    };

    useEffect(() => {
        const handleClickOutside = (event) => {
            if (userMenuRef.current && !userMenuRef.current.contains(event.target)) {
                setIsMenuOpen(false);
            }
        };

        document.addEventListener("mousedown", handleClickOutside);
        return () => document.removeEventListener("mousedown", handleClickOutside);
    }, []);

    const placeholderImg = userPlaceholder;

    return(
        <div className="header">
            <div onClick={() => navigate("/dashboard")}>
                <img src={logo} alt="Logo do SIFRA" className="responsive-img"/>
            </div>
            <div className="user" style={{display: `${props.display}`}} onClick={toggleMenu} ref={userMenuRef}>
                <p>{props.username}</p>
                <div className="user-menu">
                    <img
                        className='user-img'
                        src={props.image && props.image.trim() ? props.image : placeholderImg}
                        alt="Foto do usuário"
                        onError={(e) => { e.currentTarget.src = placeholderImg; }}
                    />
                    <span className="chevron" aria-hidden="true"></span>
                    {isMenuOpen && (
                        <div className="user-menu-card" onClick={(e) => e.stopPropagation()}>
                            <button className="user-menu-item" onClick={handleLogout}>
                                <img className='logout-icon' src={logoutIcon} alt='Ícone de logout'/>
                                <span>Sair</span>
                            </button>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
}
