import "./Barra.css";

export default function Barra(props) {
    const initials = props.name
        ? props.name
              .split(" ")
              .filter(Boolean)
              .slice(0, 2)
              .map((word) => word[0])
              .join("")
              .toUpperCase()
        : "";

    return (
        <div className="barra-box">
            <div className="barra-badge">{initials}</div>
            <div className="barra-content">
                <p className="barra-title">{props.name}</p>
                <span className="barra-code">{props.code}</span>
            </div>
            <span className="barra-chevron" aria-hidden="true"></span>
        </div>
    );
}