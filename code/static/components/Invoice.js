import { getInvoiceById } from "../methods"

export default {
    template: `
    <div>

    </div>
    `,
    data() {
        return {
            cred: {
                email: null,
                password: null,
            },
            error: null,
        }
    },
    methods: {
        login(id) {
            getInvoiceById(id)
            .then((res) => {})
        },
    },
}
