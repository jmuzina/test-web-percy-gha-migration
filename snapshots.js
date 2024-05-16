const PORT = process.env.PORT || 8101;

module.exports = () => [{
    url: `http://localhost:${PORT}/`,
    name: 'Index',
    widths: [375]
}]
