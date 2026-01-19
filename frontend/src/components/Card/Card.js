import "./Card.css";

export default function Card(props) {

    const iconMap = {
        "Cadastrar usuário": "cadastro_usuario.png",
        "Gerenciar usuários": "gerenciar_grupo.png",
        "Consultar frequência": "consultar_frequencia.png",
        "Minhas informações": "consultar_informacoes.png",
        "Gerar relatório": "gerar_relatorio.png",
        "Registro de alunos": "registro_aluno.png",
    };

    const iconName = iconMap[props.label] ?? props.icon;
    const iconSrc = require(`../../assets/icons/${iconName}`);

    return (
        <div className="card-box">
            <div className="card-icon">
                <img src={iconSrc} alt="Ícone"/>
            </div>
            <div className="card-content">
                <p className="card-title">{props.label}</p>
                {props.description ? (
                    <p className="card-description">{props.description}</p>
                ) : null}
            </div>
        </div>
    );
}