export default {
  logo: (
    <p
      style={{
        fontWeight: "bold",
      }}
    >
      MLX Server
    </p>
  ),
  project: {
    link: "https://github.com/mustafaaljadery/mlx-server",
  },
  useNextSeoProps() {
    return {
      titleTemplate: "%s – MLX Server",
    };
  },
  head: (
    <>
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <meta property="og:title" content="MLX Server" />
      <meta property="og:description" content="A server" />
    </>
  ),
  primaryHue: 301,
  primarySaturation: 33,
  footer: {
    text: (
      <span
        style={{
          fontSize: "14px",
        }}
      >
        MIT {new Date().getFullYear()} ©{" "}
        <a href="https://www.maxaljadery.com/" target="_blank">
          Mustafa Aljadery
        </a>{" "}
        &{" "}
        <a href="" target="_blank">
          Siddharth Sharma
        </a>
        .
      </span>
    ),
  },
};
